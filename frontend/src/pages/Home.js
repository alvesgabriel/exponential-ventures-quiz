import React from "react";
import Navbar from "../components/Navbar";
import Quiz from "../components/Quiz";

class Home extends React.Component {
  render() {
    return (
      <div>
        <Navbar />
        <Quiz />
      </div>
    );
  }
}

export default Home;
