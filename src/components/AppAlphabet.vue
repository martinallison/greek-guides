<template>
  <figure class="app-alphabet card">
    <figcaption class="app-alphabet-caption">The Greek alphabet</figcaption>
    <app-listen
      :src="require('@/assets/alpha.m4a')"
      class="app-alphabet-listen"
    />
    <div lang="el" class="app-alphabet-grid">
      <span v-for="pair in pairs" :key="pair[0]" class="app-alphabet-pair">
        {{ pair[0] }} {{ pair[1] }}
      </span>
    </div>
  </figure>
</template>

<script>
import AppListen from '@/components/AppListen.vue';

export default {
  components: {
    AppListen,
  },
  data() {
    return {
      upper: 'Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω'.split(' '),
      lower: 'α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ τ υ φ χ ψ ω'.split(' '),
    };
  },
  computed: {
    pairs() {
      return this.upper.map((letter, i) => [letter, this.lower[i]]);
    },
  },
};
</script>

<style lang="scss">
.app-alphabet {
  display: inline-block;
  position: relative;
  text-align: center;
  padding: $size-m;
  margin: 0;
}

.app-alphabet-caption {
  font-weight: bold;
  margin-bottom: $size-s;
}

.app-alphabet-listen {
  position: absolute;
  top: $size-xs;
  right: $size-xs;
}

.app-alphabet-grid {
  display: grid;

  @include after(600px) {
    grid-template-columns: repeat(24, min-content);
    column-gap: 5px;
  }

  @include before(600px) {
    grid-template-rows: repeat(12, 1fr);
    grid-auto-flow: column;
    grid-auto-columns: min-content;
    column-gap: $size-xl;
  }
}

.app-alphabet-pair {
  @include before(600px) {
    white-space: nowrap;
  }
}
</style>
