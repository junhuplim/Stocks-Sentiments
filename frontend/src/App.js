import { useTable, useSortBy } from "react-table";
import GetDataToTable from "./hooks/GetDataToTable";
import Table from "./components/Table";

function App() {
  const { data, columns } = GetDataToTable();
  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
  } = useTable({ columns, data }, useSortBy);
  return (
    <Table
      getTableProps={getTableProps}
      getTableBodyProps={getTableBodyProps}
      headerGroups={headerGroups}
      rows={rows}
      prepareRow={prepareRow}
    />
  );
}

export default App;
