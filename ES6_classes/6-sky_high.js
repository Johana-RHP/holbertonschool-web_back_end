import Building from "./5-building.js";

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Call the constructor of the parent class
    this._floors = floors;
  }

  // Getter for 'floors'
  get floors() {
    return this._floors;
  }

  // Override the evacuationWarningMessage method
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors.`;
  }
}

export default SkyHighBuilding;
