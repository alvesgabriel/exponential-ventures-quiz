import React, { createContext, useEffect, useState } from "react";

import api from "../../services/api";
import history from "../../services/history";

const Context = createContext();

function AuthProvider({ children }) {
  const [authenticated, setAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem("user"));

    if (user && user.token) {
      api.defaults.headers.Authorization = `Bearer ${user.token}`;
      setAuthenticated(true);
    }

    setLoading(false);
  }, [authenticated]);

  async function handleLogin(username, password) {
    const payload = {
      username: username,
      password: password,
    };

    api
      .post("login/", payload)
      .then((res) => {
        var user = res.data;
        localStorage.setItem("user", JSON.stringify(user));
        api.defaults.headers.Authorization = `Bearer ${user.token}`;
        setAuthenticated(true);
        history.push("/home");
      })
      .catch((error) => {
        console.log(error);
      });
  }

  function handleLogout() {
    localStorage.removeItem("user");
    setAuthenticated(false);
  }

  return (
    <Context.Provider
      value={{ loading, authenticated, handleLogin, handleLogout }}
    >
      {children}
    </Context.Provider>
  );
}

export { Context, AuthProvider };
