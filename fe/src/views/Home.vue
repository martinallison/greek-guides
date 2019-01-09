<template>
  <main class="main-col">
    <section>
      <h1 class="text-centre">Greek Guides</h1>

      <p>
        Come on in and learn about Modern Greek with this series of guides to
        the Modern Greek language and Greek culture in general!
      </p>

      <p>
        Written by Martin (been learning Greek for 4 years) and Maggie (an
        actual Greek person from Serres) they’ll give an insight into Greek
        without too much of the overly-technical bits.
      </p>
    </section>

    <el-intro-card/>

    <section>
      <h2>{{ basics.title }}</h2>
      <p>
        Learn enough to impress some Greeks on holiday or make your Greek partner weak at
        the knees.
      </p>

      <el-row>
        <el-subject-card
          v-for="subject in subjects"
          :key="subject.id"
          :subject="subject"
          class="el-col s-6 l-4 margin-top-s"
        />
      </el-row>
    </section>

  </main>
</template>

<script>
import chapters from '@/data/chapters';


export default {
  computed: {
    basics() {
      return chapters.find(c => c.id === 'basics');
    },
    subjects() {
      const subjects = this.$store.state.subjects.byId;
      return this.basics.subjectIds.map(id => subjects[id]);
    },
  },
};
</script>
