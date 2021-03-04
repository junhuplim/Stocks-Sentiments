import { useMemo, useEffect, useState } from "react";
import axios from 'axios'

export default function GetDataToTable() {
  const [apiData, setApiData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios(
        "http://127.0.0.1:5006/get-basic-data"
      );
      
      setApiData(result.data.data);  
    }

    fetchData(); 
  }, []); 

  const data = useMemo(
    () =>
      apiData.map((tickerData) => {
        return { ...tickerData };
      }),
    [apiData]
  );

  // console.log('hi')
  // console.log(data)

  const columns = useMemo(
    () => [
      {
        Header: "Ticker",

        accessor: "Ticker", // accessor is the "key" in the data
      },

      {
        Header: "Mentions",

        accessor: "Mentions",
      },
      {
        Header: "Name",

        accessor: "Name",
      },
      {
        Header: "Industry",

        accessor: "Industry",
      },
      {
        Header: "	Previous Close",

        accessor: "PreviousClose",
      },
      {
        Header: "5d Low",

        accessor: "Low5d",
      },
      {
        Header: "5d High",

        accessor: "High5d",
      },
      {
        Header: "1d Change",

        accessor: "ChangePercent1d",
      },
      {
        Header: "5d Change",

        accessor: "ChangePercent5d",
      },
      {
        Header: "1mo Change",

        accessor: "ChangePercent1mo",
      },
    ],
    []
  );

  return { data, columns };
}