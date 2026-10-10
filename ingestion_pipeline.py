import os

from dotenv import load_dotenv
from langchain_chroma import Croma
from langchain_community.document_loaders import DiresctoryLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
