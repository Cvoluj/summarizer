import React, { useState } from 'react';

function ChatInput({ onSend }) {
    const [text, setText] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (text.trim()) {
            onSend(text);
            setText('');
        }
    };

    return (
        <form className="chat-input" onSubmit={handleSubmit}>
            <input
                type="text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Type your message..."
            />
            <button type="submit">Send</button>
        </form>
    );
}

export default ChatInput;