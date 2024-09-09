import os
from indexer.indexer import Indexer
from retriever.retriever import Retriever
from generator.generator import Generator

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    # 移除空行和只包含空白字符的行
    data = [line.strip() for line in data if line.strip()]
    return data

def main():
    # 加载数据
    data = load_data('data/your_data.txt')
    
    print(f"加载的数据条数: {len(data)}")
    print(f"前5条数据: {data[:5]}")
    
    # 检查并清理数据
    data = [text for text in data if text is not None and text.strip()]
    
    if not data:
        print("警告：没有有效的数据可以索引。请检查您的数据文件。")
        return
    
    # 创建和保存索引
    indexer = Indexer()
    indexer.create_index(data)
    indexer.save_index('data/faiss_index.bin')
    
    # 初始化检索器和生成器
    retriever = Retriever('data/faiss_index.bin')
    generator = Generator(api_key=os.getenv('OPENAI_API_KEY'))
    
    # 用户查询
    query = input("请输入您的问题: ")
    
    # 检索相关文档
    relevant_doc_indices = retriever.retrieve(query)
    relevant_docs = [data[i] for i in relevant_doc_indices]
    
    # 生成回答
    context = "\n".join(relevant_docs)
    answer = generator.generate(context, query)
    
    print(f"回答: {answer}")

if __name__ == "__main__":
    main()