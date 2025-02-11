Here’s a refined, detailed, and categorized version of the documentation for **Ai-Web-Scraper**, including the addition of **Ollama** and its required model:

---

# **Ai-Web-Scraper**

Ai-Web-Scraper is an AI-powered web scraping tool that uses natural language processing (NLP) to extract data from websites. It is designed to be user-friendly, efficient, and scalable.

---

## **Table of Contents**

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Limitations](#limitations)
5. [Roadmap](#roadmap)
6. [Ollama Integration](#ollama-integration)

---

## **Installation**

### **Prerequisites**

-  **Google Chrome**: Ensure Google Chrome is installed on your system.
-  **Python**: Python 3.7 or higher is required.
-  **Ollama**: Required for advanced NLP capabilities.

### **Steps**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/Ai-Web-Scraper.git
   cd Ai-Web-Scraper
   ```

2. **Install Required Packages**:  
   Install the necessary Python packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install ChromeDriver**:

   -  **Mac Users**:
      ```bash
      brew install chromedriver
      ```
   -  **Windows/Linux Users**:  
      Download the correct version of ChromeDriver from the [official website](https://sites.google.com/a/chromium.org/chromedriver/) and add it to your system's PATH.

4. **Set Up Ollama**:

   -  Download and install Ollama from the [official website](https://ollama.ai/).
   -  Install the required NLP model (e.g., `ollama-model-nlp`):
      ```bash
      ollama install ollama-model-nlp
      ```
   -  Ensure Ollama is running in the background while using Ai-Web-Scraper.

5. **Verify Installation**:
   -  Ensure all dependencies are installed correctly.
   -  Test ChromeDriver by running:
      ```bash
      chromedriver --version
      ```
   -  Verify Ollama installation by running:
      ```bash
      ollama list
      ```

---

## **Usage**

### **Steps to Run the Application**

1. **Start the Application**:  
   Navigate to the cloned repository and run:

   ```bash
   streamlit run app.py
   ```

2. **Access the Web Interface**:  
   Open a web browser and go to:

   ```
   http://localhost:8501/
   ```

3. **Enter Website URL**:

   -  Input the URL of the website you want to scrape in the provided field.

4. **Start Scraping**:

   -  Click the `Scrape` button to initiate the scraping process.

5. **View Results**:
   -  The scraped data will be displayed in a table format on the web interface.

---

## **Features**

-  **AI-Powered Scraping**: Uses NLP to extract and interpret data from websites.
-  **Multi-Website Support**: Works with a variety of website types.
-  **User -Friendly Interface**: Simple and intuitive web-based interface.
-  **Scalable**: Designed to handle small to medium-sized scraping tasks efficiently.

---

## **Limitations**

-  **Browser Support**: Currently only supports Google Chrome.
-  **JavaScript-Heavy Websites**: Struggles with websites that rely heavily on JavaScript for rendering content.
-  **Model Dependency**: Requires Ollama and its NLP model for advanced features.

---

## **Roadmap**

### **Short-Term Goals**

-  Add support for multiple browsers (e.g., Firefox, Safari).
-  Improve compatibility with JavaScript-heavy websites.

### **Long-Term Goals**

-  Introduce advanced features like data filtering, sorting, and export options.
-  Enhance NLP capabilities with more sophisticated models.
-  Add support for batch scraping and scheduling.

---

## **Ollama Integration**

### **Why Ollama?**

Ollama provides advanced NLP capabilities, enabling Ai-Web-Scraper to interpret and extract data more accurately.

### **Steps to Set Up Ollama**

1. **Download Ollama**:  
   Visit the [official website](https://ollama.ai/) and download the appropriate version for your operating system.

2. **Install the NLP Model**:  
   Run the following command to install the required model:

   ```bash
   ollama install ollama-model-nlp
   ```

3. **Run Ollama**:  
   Ensure Ollama is running in the background before starting the Ai-Web-Scraper application.

4. **Verify Model Installation**:  
   Check that the model is correctly installed by running:

   ```bash
   ollama list
   ```

   This command will display the installed models, confirming that the necessary NLP model is available for use.

5. **Integrate with Ai-Web-Scraper**:  
   The Ai-Web-Scraper will automatically utilize the Ollama model during the scraping process, enhancing its data extraction capabilities.

---

## **Contributing**

We welcome contributions from the community! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.

---

## **Acknowledgements**

-  [Streamlit](https://streamlit.io/)
-  [LangChain](https://langchain.com/)
-  [LangChain Ollama](https://github.com/ollama-ai/langchain-ollama)
-  [Ollama](https://ollama.ai/)

---

## **Author**

-  [Debanjan Dutta](https://github.com/Debanjan110d)
