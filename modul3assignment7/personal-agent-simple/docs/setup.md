# 🚀 Setup & Installation Guide

## Prerequisites

### System Requirements:
- **Python**: 3.8+ (Tested on 3.13)
- **Operating System**: Windows, macOS, Linux
- **Internet**: Required untuk Gemini API calls
- **Storage**: ~100MB for dependencies + database

### API Requirements:
- **Google Gemini API Key**: Free tier available
- **Rate Limits**: Free tier = 15 requests/minute

## 📦 Installation Steps

### 1. **Clone Repository**
```bash
git clone <repository-url>
cd personal-agent-simple
```

### 2. **Create Virtual Environment** (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux  
python -m venv venv
source venv/bin/activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

#### Dependencies yang akan diinstall:
- `langchain==0.3.26` - Main framework
- `langchain-google-genai==2.1.6` - Gemini integration
- `langchain-community` - Community components
- `sqlalchemy` - Database operations
- `python-dotenv` - Environment variable management

### 4. **Setup Environment Variables**
```bash
# Copy template
cp .env.example .env

# Edit .env file
# Windows: notepad .env
# macOS/Linux: nano .env
```

#### .env File Content:
```env
# Gemini API Configuration
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

### 5. **Get Gemini API Key**

#### Steps:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in dengan Google account
3. Click "Create API Key"
4. Copy the generated key
5. Paste ke .env file

#### API Key Format:
```
GOOGLE_API_KEY=AIzaSyBTD2xwDnRtvK92R5f7HJ6DvwHQh7fiECs
```

### 6. **Verify Installation**
```bash
python -c "from langchain_google_genai import ChatGoogleGenerativeAI; print('✅ Installation successful')"
```

### 7. **Run Agent**
```bash
python agent.py
```

#### Expected Output:
```
✅ API key loaded successfully from .env file
🧠 Personal Assistant Agent (type 'exit' to quit)
Try: 'hello aya', 'what time is it', or any other question!
You:
```

## 🔧 Configuration Options

### Model Configuration:
```python
# In agent.py, you can modify:
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Model name
    temperature=0.2            # Creativity level (0-1)
)
```

#### Available Models:
- `gemini-1.5-flash` ✅ (Recommended, free)
- `gemini-1.5-flash-8b` (Smaller, faster)
- `gemini-1.5-pro` (More capable, limited free usage)

### Memory Configuration:
```python
# Adjust memory settings:
memory = ConversationBufferMemory(
    chat_memory=history,
    memory_key="chat_history",
    input_key="input",
    return_messages=True,
    max_token_limit=2000  # Adjust context window
)
```

## 🐛 Troubleshooting

### Common Issues:

#### 1. **Import Errors**
```bash
ImportError: cannot import name 'SQLiteChatMessageHistory'
```
**Solution:**
```bash
pip install langchain-community
```

#### 2. **API Key Not Found**
```bash
⚠️  Error: GOOGLE_API_KEY not found!
```
**Solution:**
- Verify .env file exists
- Check API key format
- Ensure no quotes around the key

#### 3. **Model Not Found**
```bash
404 models/gemini-pro is not found
```
**Solution:**
```python
# Change model in agent.py:
model="gemini-1.5-flash"  # Instead of "gemini-pro"
```

#### 4. **Tool Validation Error**
```bash
ValueError: ConversationalAgent does not support multi-input tool
```
**Solution:**
- Restart the agent
- Check tools.py for proper Tool definitions

#### 5. **Memory Issues**
```bash
Error: Missing some input keys: {'chat_history'}
```
**Solution:**
```bash
# Delete existing database and restart:
rm memory.db
python agent.py
```

### Debug Mode:

Enable verbose logging:
```python
# In agent.py:
agent = initialize_agent(
    tools=TOOLS,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True  # Shows detailed execution
)
```

## 🧪 Testing Installation

### Basic Tests:

#### 1. **Test API Connection**
```python
python -c "
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
response = llm.invoke('Hello')
print('✅ API Connection successful')
"
```

#### 2. **Test Database**
```python
python -c "
from langchain_community.chat_message_histories.sql import SQLChatMessageHistory
history = SQLChatMessageHistory(session_id='test', connection='sqlite:///test.db')
history.add_user_message('Test message')
print('✅ Database working')
"
```

#### 3. **Test Tools**
```python
python -c "
from tools import TOOLS
print(f'✅ {len(TOOLS)} tools loaded successfully')
for tool in TOOLS:
    print(f'  - {tool.name}: {tool.description}')
"
```

### Interactive Testing:

Run the agent and test:
```
You: hello world
Agent: Hello, world! How can I help you today?

You: what time is it
Agent: The current time is 2025-07-01 14:30:25.

You: exit
Goodbye!
```

## 📁 Project Structure

```
personal-agent-simple/
├── agent.py              # Main application
├── tools.py              # Tool definitions
├── memory.py             # (Reserved for future use)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── .env.example         # Environment template
├── .gitignore           # Git ignore rules
├── memory.db            # SQLite database (auto-generated)
├── README.md            # Project overview
└── docs/                # Documentation
    ├── README.md        # Documentation index
    ├── architecture.md  # System architecture
    ├── memory-approach.md # Memory system
    ├── strategy.md      # Implementation strategy
    ├── results-reflection.md # Results and lessons
    └── setup.md         # This file
```

## 🔒 Security Best Practices

### API Key Security:
- ✅ Never commit .env file to git
- ✅ Use environment variables for production
- ✅ Rotate API keys regularly
- ✅ Monitor API usage

### Database Security:
- ✅ SQLite file permissions (read/write owner only)
- ✅ Regular database backups
- ✅ Consider encryption for sensitive conversations

### Network Security:
- ✅ Use HTTPS for API calls (automatic)
- ✅ Monitor network traffic
- ✅ Consider firewall rules for production

## 🚀 Production Deployment

### Environment Variables:
```bash
# Production .env
GOOGLE_API_KEY=your_production_api_key
DATABASE_URL=sqlite:///production.db
LOG_LEVEL=INFO
```

### Process Management:
```bash
# Using systemd (Linux)
# Create: /etc/systemd/system/personal-agent.service

[Unit]
Description=Personal AI Agent
After=network.target

[Service]
Type=simple
User=your-user
WorkingDirectory=/path/to/personal-agent-simple
Environment=PATH=/path/to/venv/bin
ExecStart=/path/to/venv/bin/python agent.py
Restart=always

[Install]
WantedBy=multi-user.target
```

### Monitoring:
```python
# Add to agent.py for production:
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent.log'),
        logging.StreamHandler()
    ]
)
```

## 📞 Support & Resources

### Getting Help:
1. **Check Documentation**: Start with [docs/README.md](README.md)
2. **Common Issues**: See [results-reflection.md](results-reflection.md)
3. **Architecture Questions**: See [architecture.md](architecture.md)

### Useful Links:
- [LangChain Documentation](https://python.langchain.com/)
- [Google AI Studio](https://makersuite.google.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

### Community Resources:
- [LangChain Discord](https://discord.gg/langchain)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [Google AI Community](https://developers.googleblog.com/2023/12/gemini-api-developer-competition.html)

## 🔄 Updates & Maintenance

### Regular Updates:
```bash
# Update dependencies (monthly)
pip install --upgrade -r requirements.txt

# Check for deprecation warnings
python agent.py 2>&1 | grep -i deprecation

# Backup database
cp memory.db memory_backup_$(date +%Y%m%d).db
```

### Version Management:
```bash
# Check current versions
pip freeze | grep -E "(langchain|google)"

# Update specific packages
pip install --upgrade langchain-google-genai
```

### Database Maintenance:
```sql
-- Check database size
.databases

-- Vacuum database (optimize)
VACUUM;

-- Check conversation count
SELECT COUNT(*) FROM message_store;
```

---

**Congratulations! 🎉** Your Personal AI Agent is now ready to use. Start chatting and explore the capabilities!

For advanced usage and customization, check out the other documentation files in the `docs/` folder.
