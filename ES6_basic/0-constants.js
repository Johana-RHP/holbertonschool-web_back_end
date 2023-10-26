// constants.js
export function taskFirst() {
  const task = 'I prefer const when I can.'; // Usando const en lugar de var
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let'; // Usando let en lugar de var
  combination += getLast();

  return combination;
}
