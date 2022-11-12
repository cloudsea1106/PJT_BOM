import React, { useState, useEffect, useRef } from "react";

// import { useLocation } from "react-router-dom";

import SideBar from "components/molecules/common/SideBar";
import HeadBar from "components/molecules/common/Headbar";
import PatientSearchBar from "components/molecules/PatientList/PatientSearchBar";
import PatientList from "components/molecules/common/PatientList";

// api
import { requestPatientList, requestSearchPatient } from "api/patients";

function Patients() {
  const [component, setComponent] = useState(0);
  const [patientList, setPatientList] = useState([]);
  const [count, setCount] = useState(1);
  // const [page, setPage] = useState(1);
  const page = useRef(1);
  const [keyword, setKeyword] = useState("");
  // const [patientListTimerID, setPatientListTimerID] = useState("");
  const patientListTimerID = useRef([]);

  // 응답받고 데이터 확인해서 쓰지 않는 값이면 setTimeout 걸지 말기
  function patientListSuccess(res) {
    console.log("응답 받음", res.data.now, patientListTimerID.current);
    setPatientList(res.data.results);
    setCount(res.data.count);
    page.current = res.data.now;
    for (let timer of patientListTimerID.current) {
      clearTimeout(timer);
    }
    patientListTimerID.current = [];
    console.log("재요청 보냄", page.current);
    if (keyword === "") {
      const timerID = setTimeout(
        requestPatientList,
        10000,
        page.current,
        9,
        patientListSuccess,
        patientListFail
      );
      patientListTimerID.current = [...patientListTimerID.current, timerID];
      console.log("타이머 아이디 바뀜", patientListTimerID.current);
    } else {
      const timerID = setTimeout(
        requestSearchPatient,
        10000,
        page.current,
        9,
        keyword,
        patientListSuccess,
        patientListFail
      );
      // setPatientListTimerID(timerID);
      // console.log("setTimeout", page, keyword);
      // patientListTimerID.current.push(timerID);
      patientListTimerID.current = [...patientListTimerID.current, timerID];
      console.log("타이머 아이디 바뀜", patientListTimerID.current);
    }
  }

  function patientListFail(err) {
    console.log("실패", err);
  }

  useEffect(() => {
    console.log("환자 리스트 요청 보냄", page.current);
    requestPatientList(page.current, 9, patientListSuccess, patientListFail);
    return () => {
      console.log("타이머 kill", patientListTimerID);
      for (let timer of patientListTimerID.current) {
        clearTimeout(timer);
      }
      patientListTimerID.current = [];
    };
  }, []);

  function handlePageChange(clickedPage) {
    console.log(clickedPage);
    // console.log("타이머 kill", patientListTimerID);
    // clearTimeout(patientListTimerID.current);
    // setPatientListTimerID("");
    page.current = clickedPage;
    requestSearchPatient(
      page.current,
      9,
      keyword,
      patientListSuccess,
      patientListFail
    );
  }

  function onSearch() {
    // console.log("타이머 kill", patientListTimerID);
    // clearTimeout(patientListTimerID.current);
    console.log("검색해서 요청 보냄", keyword);
    requestSearchPatient(1, 9, keyword, patientListSuccess, patientListFail);
  }

  function onKeyPressSearch(event) {
    if (event.key === "Enter") {
      // console.log("타이머 kill", patientListTimerID);
      // clearTimeout(patientListTimerID.current);
      console.log("엔터 눌러서 검색한다", keyword);
      requestSearchPatient(1, 9, keyword, patientListSuccess, patientListFail);
    }
  }
  return (
    <>
      {component === 0 && (
        <div className="grid grid-cols-6 bg-back rounded-[20px] shadow-bg w-[97vw] h-[95vh] my-[2.5vh] mx-[1.5vw] font-suit">
          <SideBar />
          <div className="info-zone col-span-5">
            <HeadBar />
            <div className="flex flex-col justify-center items-center h-[84vh]">
              <div className="h-[12vh] w-full">
                <PatientSearchBar
                  keyword={keyword}
                  onChangeInput={(e) => setKeyword(e.target.value)}
                  onSearch={onSearch}
                  onKeyPress={onKeyPressSearch}
                />
              </div>
              <div className="px-8 h-[72vh] pb-4 w-full">
                <PatientList
                  patientList={patientList}
                  page={page.current}
                  count={count}
                  limit={9}
                  handlePageChange={handlePageChange}
                  nowPage="patients"
                  onZoom={() => setComponent(1)}
                  onOff={false}
                />
              </div>
            </div>
          </div>
        </div>
      )}
      {component === 1 && (
        <div className="w-[97vw] h-[95vh] my-[2.5vh] mx-[1.5vw]">
          <PatientList
            patientList={patientList}
            page={page.current}
            count={count}
            limit={9}
            handlePageChange={handlePageChange}
            nowPage="patients"
            onZoom={() => setComponent(0)}
            onOff={true}
          />
        </div>
      )}
    </>
  );
}

export default Patients;
