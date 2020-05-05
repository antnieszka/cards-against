/* eslint-disable no-new */
new Vue({
    el: '#room',
    delimiters: ['[[', ']]'],
    data: {
        message: 'Entered Room 1!',
        socket: null,
        roomError: null,
    },
    mounted: function () {
        console.log("Initializing websocket");
        this.socket = new WebSocket('ws://' + window.location.host + '/room/')
        this.socket.onmessage = this.parseResponse;
        this.socket.onclose = function (e) {
            console.error("Socket closed");
            this.roomError = e;
            console.debug(e);
        }
    },
    methods: {
        ping: function () {
            this.socket.send("hello");
        },
        parseResponse: function (response) {
            console.info(JSON.parse(response.data));
        }
    }
})