const user_id = JSON.parse($('#user-id').text());
const receiver_id = JSON.parse($('#receiver-id').text());
// Scrolling to the bottom
//
// $("#chatView").scrollTop($("#chatView").height());

const OldOnMessageEvent = index.onmessage;

index.onopen = () => {
    $('#send-btn').on('click', e => {
        const receiver_id = JSON.parse($('#receiver-id').text());
        e.preventDefault();
        const messageInput = $('input#message');
        const messageText = messageInput.val();
        if (messageText.trim() === '') {
            return;
        }
        const data = {
            message: messageText,
            sender_id: user_id,
            receiver_id: receiver_id
        }
        index.send(JSON.stringify(data));
        addMessage(data);
        messageInput.val('');
    });
}

index.onmessage = e => {
    OldOnMessageEvent(e);
    addMessage(JSON.parse(e.data));
}

function addMessage(message) {
    const chatBox = $('#chatView');
    const messageGroups = chatBox.children('.message-group');
    if (messageGroups.length > 0) {
        const lastSenderId = Number($('#last-sender-id').text());
        if (lastSenderId === message.sender_id) {
            if (lastSenderId === user_id) {
                messageGroups.children("div").append(`
                    <p class="small p-2 ms-3 mb-1 rounded-3">${message.message}</p>
                `);
            } else {
                messageGroups.children("div").append(`
                    <p class="small p-2 ms-3 mb-1 rounded-3"  style="background-color: #f5f6f7;">${message.message}</p>
                `);
            }
        } else {
            if (lastSenderId === user_id) {
                chatBox.append(`
                    <div class="message-group d-flex flex-row justify-content-end mb-4 pt-1" data-user="${user_id}">
                        <div>
                            <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">${message.message}</p>
                        </div>
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava4-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                    </div>
                `);
            } else {
                chatBox.append(`
                    <div class="message-group d-flex flex-row justify-content-start mb-4" data-user="${receiver_id}">
                        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                        <div>
                            <p class="small p-2 ms-3 mb-1 rounded-3"  style="background-color: #f5f6f7;">${message.message}</p>
                        </div>
                    </div>
                `);
            }
        }
    } else {
        if (message.sender_id === user_id) {
            chatBox.append(`
                <div class="message-group d-flex flex-row justify-content-end mb-4 pt-1" data-user="${user_id}">
                    <div>
                        <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary" style="background-color: #f5f6f7;">${message.message}</p>
                    </div>
                    <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava4-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                </div>
            `);
        } else {
            chatBox.append(`
                <div class="message-group d-flex flex-row justify-content-start mb-4" data-user="${receiver_id}">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp" alt="avatar 1" style="width: 45px; height: 100%;">
                    <div>
                        <p class="small p-2 ms-3 mb-1 rounded-3">${message.message}</p>
                    </div>
                </div>
            `);
        }
    }
}