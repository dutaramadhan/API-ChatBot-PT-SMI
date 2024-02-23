<h1 align="center">API Chatbot PT SMI</h1>

## Table of Contents
1. [Information About API](#api-info)
2. [Our Main Feature](#main-feature)

   a. [Chat Completions](#chat-completions)

   b. [Function Calling](#function-calling)

   c. [Embedding and Vector Search](#embedding)
3. [System's Flow](#systems-flow)
4. [Tech Stack](#tech-stack)
5. [How to Run Locally](#run-local)
6. [How to Deploy](#deploy)
7. [Live Instance](#live-instance)
8. [API Endpoint](#endpoint)
9. [Related Repository](#related-repo)

<a name="api-info"></a>
## Information About this API
API ini berfungsi untuk melakukan proses Chat Completion dengan memanfaatkan fitur Function Calling dan model "gpt-3.5-turbo-1106" dari OpenAI. Pengguna dapat memasukan input berupa query pertanyaan pada parameter API. Server akan memanggil <a href='https://github.com/dutaramadhan/API-Query-Data-PT-SMI'>API Query Data</a> untuk melakukan embedding terhadap input dan melakukan query atau retrieval sepuluh data dari database berdasarkan simmilarity atau kemiripan tertinggi dengan input. Sepuluh data tersebut akan digunakan sebagai tambahan pengetahuan untuk chatbot. Berdasar sepuluh data tersebut, sistem Chat Completion atau Function Calling akan menjawab pertanyaan dari pengguna. Hasil atau response akan di-deliver kepada pengguna dalam format JSON.

<a name="main-feature"></a>
## Main Features
<a name="chat-completions"></a>
### a. Chat Completions
Fitur untuk melengkapi atau menyelesaikan percakapan dengan menggunakan algoritma pemodelan bahasa untuk menghasilkan teks yang koheren dan relevan berdasarkan input pengguna. Nodel yang digunakan pada sistem ini adalah "gpt-3.5-turbo-1106" dari OpenAI. Fitur ini dapat memahami konteks percakapan dan merespons dengan jawaban atau prediksi yang sesuai.
<a name="function-calling"></a>
### b. Function Calling
Fitur dari API Chat Completions OpenAI yang memungkinkan pengguna untuk mendeskripsikan fungsi-fungsi yang ingin dipanggil dalam sebuah pemanggilan API. API akan secara pintar menentukan fungsi mana yang perlu dipanggil berdasarkan input yang diberikan, dan kemudian menghasilkan JSON yang berisi argumen-argumen yang diperlukan untuk memanggil satu atau beberapa fungsi tersebut. Namun, perlu dicatat bahwa dalam proses ini, API tidak langsung memanggil fungsi tersebut, melainkan hanya menghasilkan JSON yang dapat digunakan oleh pengguna untuk memanggil fungsi tersebut di dalam kode.
<a name="embedding"></a>
### c. Embedding dan Vector Search
Fitur untuk mencari tambahan pengetahuan berdasar simmilarity setiap data di dalam database dengan query pertanyaan pengguna. Fitur ini memanggil API yang sudah ada sebelumnya, yaitu <a href='https://github.com/dutaramadhan/API-Query-Data-PT-SMI'>API Query Data</a>

<a name="systems-flow"></a>
## System's Flow

<a name="tech-stack"></a>
## Tech Stack
### 1. Python
### 2. Flask
### 3. OpenAI
### 4. Docker

<a name="run-local"></a>
## How to Run Locally
1. Clone repositori ini
   ```
   git clone https://github.com/dutaramadhan/API-Query-Data-PT-SMI.git
   ```
2. Ikuti cara set up dan run yang ada di dokumentasi
3. Clone repositori ini
   ```
   git clone https://github.com/dutaramadhan/API-ChatBot-PT-SMI.git
   ```
4. Buka direktori API-Query-Data-PT-SMI
5. Install pyhton virtual environtment 
   ```
   pip install virtualenv
   ```
6. Buat virtual environment
   ```
   virtualenv venv
   ```
7. Aktifkan virtual environment
   - Windows
     ```
     venv/Scripts/activate
     ```
   - Linux/macOS
     ```
     source venv/bin/activate
     ```
8. Install semua library atau depedensi yang dibutuhkan
   ```
   pip install -r requirements.txt
   ```
9. Buat file .env
   ```
   API_KEY = ...
   API_QUERY_URL = ...
   ```
10. Jalankan aplikasi
    ```
    python app.py
    ```
11. Cek apakah server sedang berjalan
    ```
    http://localhost:5000/
    ```

<a name="deploy"></a>
## How to Deploy
1. Buat file .env
   ```
   API_KEY = ...
   API_QUERY_URL = ...
   ```
2. Build docker image
   ```
   docker build -t api-chatbot .
   ```
3. Run docker image
   ```
   docker run -d -p 5002:5002 --name api-chatbot api-chatbot
   ```
4. Cek apakah server sedang berjalan
    ```
    http://<ip-host>:5002/
    ```

<a name="live-instance"></a>
## Live Instance
http://10.10.6.69:5002

<a name="endpoint"></a>
## API Endpoint
### 1. chatbot
   Get chatbot response based on query
 - ##### Route
   ```
   GET /smi/chatbot
   ```

- ##### Parameters
  ```
  query: string
  ```

- ##### Response
  ```
    Ntar baru down servernya
  ```
### 2. chatbot with history
   Get chatbot response based on query and mantain previous chat context history
 - ##### Route
   ```
   POST /smi/chatbot
   ```

- ##### Parameters
  ```
  query: string
  ```
  
- ##### body json
  ```
  {
     "history": [{
        "role": "user" OR "assistant",
        "content": string
     }]
  }
  ```

- ##### Response
  ```
    Ntar baru down servernya
  ```

<a name="related-repo"></a>
## Related Repository
- <a href='https://github.com/dutaramadhan/API-Query-Data-PT-SMI'>API-Query-Data-PT-SMI</a>
- <a href='https://github.com/dutaramadhan/API-Otomasi-ETL-PT-SMI'>API-Otomasi-ETL-PT-SMI</a>
