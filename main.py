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
from src.packages.utils.db_utils import create_db, get_db, get_all_files, get_file_by_id, get_file_by_name, delete_file_by_id


# Loading environment variables from .env file
load_dotenv()


# logging.basicConfig(filename='app.log', level=logging.INFO)
# app = FastAPI()

# @app.post("/chat", response_model=QueryResponse)
# def chat(query_input: QueryInput):
#     session_id = query_input.session_id
#     logging.info(f"Session ID: {session_id}, User Query: {query_input.question}, Model: {query_input.model.value}")
#     if not session_id:
#         session_id = str(uuid.uuid4())

    

#     chat_history = get_chat_history(session_id)
#     rag_chain = get_rag_chain(query_input.model.value)
#     answer = rag_chain.invoke({
#         "input": query_input.question,
#         "chat_history": chat_history
#     })['answer']
    
#     insert_application_logs(session_id, query_input.question, answer, query_input.model.value)
#     logging.info(f"Session ID: {session_id}, AI Response: {answer}")
#     return QueryResponse(answer=answer, session_id=session_id, model=query_input.model)

# from fastapi import UploadFile, File, HTTPException
# import os
# import shutil

# @app.post("/upload-doc")
# def upload_and_index_document(file: UploadFile = File(...)):
#     allowed_extensions = ['.pdf', '.docx', '.html']
#     file_extension = os.path.splitext(file.filename)[1].lower()
    
#     if file_extension not in allowed_extensions:
#         raise HTTPException(status_code=400, detail=f"Unsupported file type. Allowed types are: {', '.join(allowed_extensions)}")
    
#     temp_file_path = f"temp_{file.filename}"
    
#     try:
#         # Save the uploaded file to a temporary file
#         with open(temp_file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)
        
#         file_id = insert_document_record(file.filename)
#         success = index_document_to_chroma(temp_file_path, file_id)
        
#         if success:
#             return {"message": f"File {file.filename} has been successfully uploaded and indexed.", "file_id": file_id}
#         else:
#             delete_document_record(file_id)
#             raise HTTPException(status_code=500, detail=f"Failed to index {file.filename}.")
#     finally:
#         if os.path.exists(temp_file_path):
#             os.remove(temp_file_path)

# @app.get("/list-docs", response_model=list[DocumentInfo])
# def list_documents():
#     return get_all_documents()

# @app.post("/delete-doc")
# def delete_document(request: DeleteFileRequest):
#     # Delete from Chroma
#     chroma_delete_success = delete_doc_from_chroma(request.file_id)

#     if chroma_delete_success:
#         # If successfully deleted from Chroma, delete from our database
#         db_delete_success = delete_document_record(request.file_id)
#         if db_delete_success:
#             return {"message": f"Successfully deleted document with file_id {request.file_id} from the system."}
#         else:
#             return {"error": f"Deleted from Chroma but failed to delete document with file_id {request.file_id} from the database."}
#     else:
#         return {"error": f"Failed to delete document with file_id {request.file_id} from Chroma."}
