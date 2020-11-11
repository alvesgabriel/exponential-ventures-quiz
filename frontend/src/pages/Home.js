import React from "react";

class Home extends React.Component {
  render() {
    var user = JSON.parse(localStorage.getItem("user"));
    return <h1>Hello {user.name}</h1>;
  }
}

export default Home;
