<template>
  <figure class="alphabet card">
    <p>Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω</p>
    <p>α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ,ς τ υ φ χ ψ ω</p>
  </figure>
</template>

<script>
export default {
};
</script>

<style lang="scss" scoped>
.alphabet {
  font-family: $font-greek;
  font-weight: bold;
  padding: $space-s $space-s;
  text-align: center;

  p {
    letter-spacing: 0.03rem;
  }
}
</style>
