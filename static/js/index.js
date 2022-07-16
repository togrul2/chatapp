const socket_url_protocol = window.location.protocol === 'https:' ? 'wss' : 'ws';

const index = new WebSocket(`${socket_url_protocol}://${window.location.host}/chat/`);

index.onmessage = e => {
	// TODO can handle message popup here
    let data = JSON.parse(e.data);
    console.log(data);
};
