import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardContent from "@material-ui/core/CardContent";
import Typography from "@material-ui/core/Typography";

import history from "../services/history";

const useStyles = makeStyles({
  root: {
    minWidth: 300,
    margin: 10,
    flex: 1,
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

export default function SimpleCard(data) {
  const classes = useStyles();

  function handleQuestion(quiz) {
    history.push("question/", quiz);
  }

  return (
    <Card className={classes.root}>
      <CardActionArea
        onClick={(event) => {
          handleQuestion(data.quiz);
        }}
      >
        <CardContent>
          <Typography variant="h5" component="h2">
            {data.quiz.name}
          </Typography>
          <Typography variant="body2" component="p">
            {data.quiz.description}
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
