import React from "react";
import Navbar from "../components/Navbar";
import Question from "../components/Question";

class Questions extends React.Component {
  render() {
    return (
      <div>
        <Navbar />
        <Question />
      </div>
    );
  }
}

export default Questions;
