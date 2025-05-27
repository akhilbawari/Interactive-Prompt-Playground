# 🔍 GPT Parameter Playground

This Python script tests various combinations of OpenAI GPT model parameters and generates product descriptions based on a fixed prompt. It helps explore how model settings like `temperature`, `max_tokens`, `presence_penalty`, and `frequency_penalty` affect output.

---

## 🧠 What It Does

- Uses OpenAI's Chat Completions API (`gpt-3.5-turbo` or `gpt-4`)
- Iterates through combinations of:
  - `temperature`: [0.0, 0.7, 1.2]
  - `max_tokens`: [50, 150, 300]
  - `presence_penalty`: [0.0, 1.5]
  - `frequency_penalty`: [0.0, 1.5]
- Sends a prompt asking the model to generate a product description for the iPhone 13 Pro
- Stores responses along with their parameter settings in a CSV file
- Prints a preview table of the first 10 results in markdown format

---

## 📦 Output

- A CSV file `playground.csv` with:
  - All parameter settings
  - Generated text output
- A Markdown-style preview of the first 10 outputs printed to the console

---

## 🛠️ Setup Instructions

1. **Clone the repository or copy the script into a `.py` file**

2. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file with your OpenAI API key:**

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

---

## 🚀 Run the Script

```bash
python3 playground.py
```

---

## ✏️ Customize

- Change the `user_prompt` to test different input scenarios.
- Adjust parameter ranges to explore additional combinations.
- Switch the model between `gpt-3.5-turbo` and `gpt-4` as needed.

---

## 📁 Example Prompt Used

**System Prompt:**
```
You are a professional product marketing specialist. Create compelling, accurate product descriptions.
```

**User Prompt:**
```
Create a product description for: Iphone 13 pro.
```

---

## ✅ Example Output Row

| Temperature | Max Tokens | Presence Penalty | Frequency Penalty | Output                                |
|-------------|-------------|------------------|--------------------|----------------------------------------|
| 0.7         | 150         | 0.0              | 0.0                | iPhone 13 Pro delivers stunning...     |

---
