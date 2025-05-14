import os
import sys
import uuid
import shutil
import logging
from dotenv import load_dotenv
from src.packages.utils.chroma_utils import vectorstore
from src.packages.utils.pydantic_models import ModelName
from src.packages.langchain.langchain_utils import get_rag_chain
from src.packages.utils.pydantic_models import QueryInput, QueryResponse, DeleteFileRequest
from src.packages.utils.db_utils import ( create_db, get_db, get_all_files, get_file_by_id, get_file_by_name, delete_file_by_id,)


# Loading environment variables from .env file
load_dotenv()






