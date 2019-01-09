<template>
  <div class="crossword-container">
    <table class="crossword">
      <tr v-for="(row, rowNumber) in grid" :key="`row-${rowNumber}`">
        <td
          v-for="(cell, cellNumber) in row"
          :key="`row-${rowNumber}.col-${cellNumber}`"
          :class="{ 'letter-cell': !!cell.letter }"
        >
          <span v-if="cell.found">{{ cell.letter }}</span>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    crossword: {
      required: true,
    },
  },
  computed: {
    crosswordGrid() {
      const entries = Object
        .entries(this.crossword.placements)
        .sort((el, other) => el[1].found ? 1 : -1);

      return entries
        .reduce((acc, [word, placement]) => {
          Array.prototype.forEach.call(word, (letter, i) => {
            const x = placement.x + (i * placement.orient[0]);
            const y = placement.y + (i * placement.orient[1]);

            acc[`${x},${y}`] = {
              letter,
              found: placement.found
            };
          });

          return acc;
        }, {});
    },
    emptyGrid() {
      return Array(this.crossword.height).fill(null)
        .map(el => Array(this.crossword.width).fill(null));
    },
    grid() {
      return this.emptyGrid.map((row, i) => {
        return row.map((cell, j) => {
          const c = this.crosswordGrid[`${j},${i}`];
          return {
            letter: c && c.letter,
            found: c && c.found,
          };
        });
      });
    },
  },
}
</script>

<style lang="scss">
.crossword {
  font-size: 0.8rem;
  border-spacing: 2px;
  margin: 0 auto;
  text-align: center;

  td {
    width: 1em;
    height: 1em;
  }

  .letter-cell {
    border: 0;
    border-radius: 5px;
    background: #1edeb5;
    color: white;
    font-weight: 500;
  }
}
</style>
