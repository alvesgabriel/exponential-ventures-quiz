import React from "react";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import { Button } from "@material-ui/core";

import "./Question.css";

import api from "../services/api";
import history from "../services/history";

class Question extends React.Component {
  state = {
    resData: {},
    loading: true,
  };

  componentDidMount() {
    const quiz_id = history.location.state.id;

    api
      .get(`quizzes/${quiz_id}/questions/`)
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

  handleSubmit(event) {}

  render() {
    const { resData, loading } = this.state;

    if (loading) {
      return <h1>loading...</h1>;
    }

    if (resData.results.length === 0) {
      return <h1>No questions</h1>;
    }

    return (
      <form onSubmit={this.handleSubmit}>
        {resData.results.map((question) => (
          <div className="question" component="fieldset" key={question.id}>
            <FormLabel component="legend">{question.asking}</FormLabel>
            <RadioGroup>
              <FormControlLabel
                value="answer1"
                control={<Radio />}
                label={question.answer1}
              />
              <FormControlLabel
                value="answer2"
                control={<Radio />}
                label={question.answer2}
              />
              <FormControlLabel
                value="answer3"
                control={<Radio />}
                label={question.answer3}
              />
              <FormControlLabel
                value="answer4"
                control={<Radio />}
                label={question.answer4}
              />
            </RadioGroup>
          </div>
        ))}
        <Button type="submit" variant="outlined" color="primary">
          Submit
        </Button>
      </form>
    );
  }
}

export default Question;
