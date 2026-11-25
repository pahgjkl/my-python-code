import pymupdf
def read_pdf(path):
    try:
        doc = pymupdf.open(path)
        for page in doc:
            yield page.get_text()
    except Exception as e:
        print(f"读取错误:{e}")