<div id="room">
    <h2 v-if="roomError !== null">[[ roomError ]]</h2>
    <div>
        [[ message ]]
    </div>

    <div>
        Current socket: [[ socket.url ]]
    </div>

    <button type="button" @click="ping()">Ping</button>

</div>
