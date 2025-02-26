import Message from "./Message";
import ListGroup from "./components/ListGroup";


function App() {
  let data_points = ["1", "2", "3", "4", "5"];
  let data_points2 = ["4", "4", "3", "4", "5"];

  const handleSelectDataPoint = (data_point: string) => {
    console.log(data_point);
  };
  return (
    <>
      {" "}
      {/* <-- This is a fragment */}
      {/* This is a JSX comment */}
      <Message />
      <ListGroup data_points={data_points} heading="Data Points" onSelectDataPoint={handleSelectDataPoint} />
      <ListGroup data_points={data_points2} heading="2nd Data Points" onSelectDataPoint={handleSelectDataPoint}/>
    </>
  );
}
export default App;
