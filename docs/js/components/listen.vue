<template>
    <div>
        <audio ref="audio"
               :src="$g.getUrl('/audio/' + word + '.m4a')"
               v-on:playing="playing = true"
               v-on:ended="playing = false">
        </audio>
        <span v-if="playing">👂</span>
        <a v-if="!playing" href="#" @click.prevent="$refs.audio.play()">
            <img class="listen"
                 :src="$g.getUrl('/img/audio.svg')"
                 :alt="'listen to pronunciation of ' + word">
        </a>
    </div>
</template>

<script>
    const Listen = {
        name: "listen",
        props: ["word"],
        data: () => {
            return {
                playing: false
            }
        },
    };

    export default Listen;
</script>