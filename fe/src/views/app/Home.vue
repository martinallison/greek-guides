<template>
  <main class="main-col">
    <section>
      <h1 class="text-centre">Greek Guides</h1>

      <p>
        Come on in and learn about Modern Greek! These guides to the language (and Greek
        culture in general) are written by a Greek native and someone learning the language
        (slowly and lazily).
      </p>
    </section>

    <section>
      <el-intro-card/>
    </section>

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
