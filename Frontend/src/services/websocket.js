const WS_URL =
  import.meta.env.VITE_SIMULATOR_WS ||
  "ws://127.0.0.1:9000/ws";


export function createWebSocket(
  onMessage,
  onStatus
) {

  const socket = new WebSocket(WS_URL);

  socket.onopen = () => {

    console.log(
      "Simulation WebSocket connected"
    );

    if (onStatus) {
      onStatus("CONNECTED");
    }
  };


  socket.onmessage = (message) => {

    try {

      const data = JSON.parse(
        message.data
      );

      onMessage(data);

    } catch (error) {

      console.error(
        "Invalid WebSocket message",
        error
      );
    }
  };


  socket.onerror = () => {

    if (onStatus) {
      onStatus("ERROR");
    }
  };


  socket.onclose = () => {

    if (onStatus) {
      onStatus("DISCONNECTED");
    }
  };


  return socket;
}