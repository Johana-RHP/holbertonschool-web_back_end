import ClassRoom from './0-classroom.js';

function initializeRooms() {
  const rooms = [19, 20, 34].map((size) => new ClassRoom(size));
  return rooms;
}

export default initializeRooms;
