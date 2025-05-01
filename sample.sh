curl "https://api.llama.com/v1/chat/completions" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $LLAMA_API_KEY" \
-d '{
      "model": "Llama-4-Maverick-17B-128E-Instruct-FP8",
      "messages": [
        {"role": "user", "content": "What is the AI Resource Program @ Alaska SBDC?"}
      ]
}'