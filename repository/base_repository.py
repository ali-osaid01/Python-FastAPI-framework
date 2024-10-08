from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Optional, Dict, Any, TypeVar, Generic
from pydantic import BaseModel
from bson import ObjectId,json_util

T = TypeVar('T', bound=BaseModel)
D = TypeVar('D', bound=BaseModel)

class BaseRepository(Generic[T, D]):
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection
        
    async def get_all(
        self,
        page: int = 1,
        limit: int = 10,
        filter: Optional[Dict[str, Any]] = None,
        project_field: Optional[Dict[str, int]] = None,
        sort: Optional[Dict[str, int]] = None,
    ) -> List[T]:
        cursor = self.collection.find(filter or {}, project_field or {})
        if sort:
            cursor = cursor.sort(list(sort.items()))
        cursor = cursor.skip((page - 1) * limit).limit(limit)
        return [item async for item in cursor]

    async def get_one(self, filter: Dict[str, Any], project_field: Optional[Dict[str, int]] = None) -> Optional[T]:
        document = await self.collection.find_one(filter, projection=project_field or {})
        if document is not None:
            document['_id'] = str(document['_id'])
            return document
        return None
    
    async def get_by_id(self, id: str) -> Optional[T]:
        document = await self.collection.find_one({"_id": ObjectId(id)})
        return document

    async def create(self, entity: D) -> Optional[T]:
        result = await self.collection.insert_one(entity.model_dump())
        return {
        "id": str(result.inserted_id),  
        **entity.model_dump()           
        }

    async def create_many(self, entities: List[D]) -> List[str]:
        result = await self.collection.insert_many([entity.model_dump() for entity in entities])
        return [str(inserted_id) for inserted_id in result.inserted_ids]

    async def update_by_id(
        self, id: str, update_data: Dict[str, Any]
    ) -> Optional[T]:
        result = await self.collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": update_data},
            return_document=True
        )
        return result

    async def update_one(
        self, filter: Dict[str, Any], update_data: Dict[str, Any]
    ) -> Optional[T]:
        result = await self.collection.find_one_and_update(
            filter, {"$set": update_data}, return_document=True
        )
        return result

    async def update_many(
        self, filter: Dict[str, Any], update_data: Dict[str, Any]
    ) -> int:
        result = await self.collection.update_many(filter, {"$set": update_data})
        return result.modified_count

    async def delete(self, filter: Dict[str, Any]) -> bool:
        result = await self.collection.delete_one(filter)
        return result.deleted_count > 0

    async def delete_many(self, filter: Dict[str, Any]) -> int:
        result = await self.collection.delete_many(filter)
        return result.deleted_count

    async def get_count(self, filter: Optional[Dict[str, Any]] = None) -> int:
        count = await self.collection.count_documents(filter or {})
        return count

    async def aggregate(self, pipeline: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        result = await self.collection.aggregate(pipeline).to_list(length=None)
        return result
