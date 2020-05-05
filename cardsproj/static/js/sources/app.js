Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        message: 'Hello Vue!',
        decks: [],
        cards: [],
        selectedDeck: null,
    },
    methods: {
        getDecks: function () {
            this.$http.get('/api/decks').then(response => {
                this.decks = response.body;
                console.log(this.decks);
            }, response => {
                console.error(response);
            });
        },
        getDeckCards: function (deckName) {
            this.$http.get('/api/cards/' + deckName).then(response => {
                this.selectedDeck = deckName;
                this.cards = response.body;
                console.log(this.cards);
            }, response => {
                console.error(response);
            });
        }
    }
})