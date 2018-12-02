import store from '@/store';


const { subjects } = store.state;

export const Guide = (guide) => {
  const subject = subjects.all.find(s => s.guideIds.indexOf(guide.id) > -1);
  const ids = subject ? subject.guideIds : [];
  const index = ids.indexOf(guide.id);

  return {
    ...guide,
    subject,
    index,
    emoji: index === 0 ? subject.emoji : null,
    prevId: ids[index - 1],
    nextId: ids[index + 1],
  };
};

export default Guide;
