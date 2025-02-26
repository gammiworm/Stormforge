import { useState } from "react";

interface Props {
  data_points: string[];
  heading: string;
  onSelectDataPoint: (data_point: string) => void;
}

function ListGroup({ data_points, heading, onSelectDataPoint }: Props) {
  const [selectedIndex, setSelectedIndex] = useState(-1);
  const [selectedIndex2, setSelectedIndex2] = useState(0);

  return (
    <>
      {" "}
      {/* <-- This is a fragment */}
      {/* This is a JSX comment */}
      <h1>{heading}</h1>
      {data_points.length === 0 && <p>"No data points"</p>}
      <ul className="list-group">
        {data_points.map((data_points, index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={data_points}
            onClick={() => {
                setSelectedIndex(index)
                setSelectedIndex2(index+2)
                onSelectDataPoint(data_points)
            }}
          >
            {data_points}
            <p className={
                selectedIndex2 === index
                    ? "list-group-item active"
                    : "list-group-item"
            }>
                "hello"
            </p>
          </li>
        ))}
      </ul>
    </>
  );
}

function getMessage() {
  return "Hello World";
}

export default ListGroup;
