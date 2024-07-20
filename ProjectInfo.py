import tempfile
import webbrowser
import os
import time
import threading

class ProjectInfo:
    def __init__(self , html_content):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html')
        self.temp_file_path = self.temp_file.name
        self.html_content = html_content
    
    def createTempFile(self):
        self.temp_file.write(self.html_content)
        self.temp_file.close()
    
    def openTempFile(self):
        webbrowser.open('file://' + self.temp_file_path)
    
    def deleteTempFile(self):
        time.sleep(60)
        os.remove(self.temp_file_path)
    
    def openTempFileInThread(self):
        self.createTempFile()
        self.openTempFile()
        t = threading.Thread(target=self.deleteTempFile)
        t.start()
        t.join()
    

if __name__ == '__main__':
    html_content = """
        <html>
            <head>
                <title>Project Info</title>
            </head>
        <body>
            <h1>Project Info</h1>
                <p>This is a sample project info page.</p>
            </body>
        </html>
    """
    project_info = ProjectInfo(html_content)
    project_info.openTempFileInThread()
    
    
