import React, { useContext } from "react";
import { Router, Route, Switch, Redirect } from "react-router-dom";
import CircularProgress from "@material-ui/core/CircularProgress";

import { Context } from "../components/Context/AuthContext";

import history from "../services/history";

import Login from "./Login";
import Home from "./Home";

function CustonRoute({ isPrivate, ...rest }) {
  const { loading, authenticated } = useContext(Context);

  if (loading) {
    return <CircularProgress />;
  }

  if (authenticated && rest.path === "/login") {
    return <Redirect to="/home" />;
  }

  if (isPrivate && !authenticated) {
    return <Redirect to="/login" />;
  }

  return <Route {...rest} />;
}

class Routes extends React.Component {
  render() {
    return (
      <Router history={history}>
        <Switch>
          <CustonRoute path="/login" component={Login} />
          <CustonRoute path="/home" isPrivate component={Home} />
        </Switch>
      </Router>
    );
  }
}

export default Routes;
