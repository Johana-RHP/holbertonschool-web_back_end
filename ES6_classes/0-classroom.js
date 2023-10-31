export default class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }
  
  // Getter method to access the maxStudentsSize attribute
  get maxStudentsSize() {
    return this._maxStudentsSize;
  }
}
