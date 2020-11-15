import React from "react";
import Navbar from "../components/Navbar";

class Home extends React.Component {
  render() {
    var user = JSON.parse(localStorage.getItem("user"));

    return (
      <div>
        <Navbar />
        <h1>Hello {user.name}</h1>
      </div>
    );
  }
}

export default Home;
