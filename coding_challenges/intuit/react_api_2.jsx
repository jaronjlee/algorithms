import React, { useState, useEffect } from "react";

export default () => {
    const [data, setData] = useState(null);

    useEffect(async () => {
        const response = await fetch("https://api.randomuser.me/");
        const data = await response.json();
        const [item] = data.results;
        setData(item);
    }, []);

    return (
        <div>
            <div>{data.name.first}</div>
        </div>
    );
};

// OR //

import React, { useState, useEffect } from "react";

const useFetch = url => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(async () => {
    const response = await fetch(url);
    const data = await response.json();
    const [item] = data.results;
    setData(item);
    setLoading(false);
  }, []);

  return { data, loading };
};

export default () => {
  const { data, loading } = useFetch("https://api.randomuser.me/");

  return (
    <div>
      {loading ? <div>...loading</div> : <div>{data.name.first}</div>}
    </div>
  );
};