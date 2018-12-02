<template>
  <figure lang="el" class="el-alphabet">
    <p class="el-alphabet-upper">Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω</p>
    <p class="el-alphabet-lower">α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ,ς τ υ φ χ ψ ω</p>
  </figure>
</template>

<script>
export default {
};
</script>

<style lang="scss">
.el-alphabet {
  font-weight: bold;
  letter-spacing: 0.03rem;
  margin-left: $space-m;
  margin-right: $space-m;
  text-align: center;
  @include card;
}

.el-alphabet-upper {
  margin-bottom: $space-xs;
}

.el-alphabet-lower {
  margin-top: 0;
}
</style>
