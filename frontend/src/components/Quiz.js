import React from "react";

import "./Quiz.css";

import api from "../services/api";

import SimpleCard from "./Card";

class Quiz extends React.Component {
  state = {
    resData: {},
    loading: true,
  };

  componentDidMount() {
    api
      .get("quizzes/")
      .then((res) => {
        this.setState({
          resData: res.data,
        });
        this.setState({ loading: false });
      })
      .catch((error) => {
        console.log(error);
      });
  }

  render() {
    const { resData, loading } = this.state;

    if (loading) {
      return <h1>loading...</h1>;
    }

    return (
      <div className="simple-card">
        {resData.results.map((quiz) => (
          <SimpleCard quiz={quiz} key={quiz.id} />
        ))}
      </div>
    );
  }
}

export default Quiz;
