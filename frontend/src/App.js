import './App.css';
import React, { useState } from 'react';
import ChatWindow from './components/ChatWindow';
import ChatInput from './components/ChatInput';
import chatService from './services/chatService';

function App() {
  const [messages, setMessages] = useState([]);

  const handleSend = async (message) => {
    const newMessage = { sender: 'user', text: message };
    setMessages([...messages, newMessage]);

    try {
        const response = await chatService.getSummary(message);
        const responseMessage = { sender: 'bot', text: response };
        setMessages((prevMessages) => [...prevMessages, responseMessage]);
    } catch (error) {
        console.error('Error fetching summary:', error);
    }
  };

  return (
    <div className="chat-app">
            <ChatWindow messages={messages} />
            <ChatInput onSend={handleSend} />
    </div>
  );
}

export default App;
