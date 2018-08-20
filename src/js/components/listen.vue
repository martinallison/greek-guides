<template>
    <div class="gr-listen" ref="container">
        <audio
            ref="audio"
            :src="audioUrl"
            v-on:playing="playing = true"
            v-on:ended="playing = false">
        </audio>

        <span class="gr-playing-icon" :style="styles.emoji" v-if="playing">👂</span>

        <a class="gr-play-button" v-if="!playing" @click.prevent="$refs.audio.play()">
            <img class="gr-play-icon" v-bind="playIcon">
        </a>
    </div>
</template>

<script>
    const Listen = {
        name: "gr-listen",
        props: {
            word: String,
            audioUrl: String,
        },
        data() {
            return {
                height: 0,
                playing: false,
            }
        },
        mounted() {
            this.$nextTick(() => {
                this.height = this.getHeight();
            });
        },
        computed: {
            playIcon() {
                return {
                    src: this.$g.getUrl("/img/audio.svg"),
                    alt: "Listen to the pronunciation of " + this.word
                };
            },
            styles() {
                return {
                    emoji: {
                        "font-size": this.height + "px",
                    },
                };
            },
        },
        methods: {
            getHeight() {
                const height = this.$refs.container.clientHeight;
                const style = window.getComputedStyle(this.$refs.container);
                const padding = {
                    top: parseInt(style.getPropertyValue("padding-top")),
                    bottom: parseInt(style.getPropertyValue("padding-bottom")),
                }
                return height - padding.top - padding.bottom;
            },
        },
    };

    export default Listen;
</script>

<style scoped lang="scss">
    .gr-listen {
        cursor: pointer;
    }

    .gr-play-button, .gr-play-icon, .gr-playing-icon {
        display: block;
        height: 100%;
        width: 100%;
    }

    .gr-playing-icon {
        line-height: 1;
        margin: 0;
        padding: 0;
    }

    .gr-listen {
        background: #76f4e1;
        padding: 6px;
        border-radius: 100%;
    }
</style>
