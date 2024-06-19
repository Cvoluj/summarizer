import React from 'react';

function ChatMessage({ message }) {
    const { sender, text } = message;
    return (
        <div className={`chat-message ${sender}`}>
            <div className="message-text">{text}</div>
        </div>
    );
}

export default ChatMessage;
