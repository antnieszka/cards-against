<div id="app">
    [[ message ]]

    <button type="button" @click="getDecks()">Get decks</button>
    <ul>
        <li v-for="deck in decks" @click="getDeckCards(deck)">
            [[ deck ]] (Click on name to download cards)
        </li>
    </ul>

    <div v-if="selectedDeck">
        <h5>Cards for deck: [[ selectedDeck ]] (count: [[ cards.length ]])</h5>
        <ul>
            <li v-for="card in cards">
                [[ card.text ]] (holes: [[card.holes]])
            </li>
        </ul>
    </div>

</div>
