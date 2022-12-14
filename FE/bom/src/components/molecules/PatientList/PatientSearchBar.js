import React from "react";

import Input from "components/atoms/Input";
import Btn from "components/atoms/Btn";

import { UilSearch } from "@iconscout/react-unicons";

function PatientSearchBar({ keyword, onChangeInput, onSearch, onKeyPress }) {
  return (
    <div className="searchbar-box grid grid-cols-10 items-center h-full py-4 px-8">
      <div className="input-box h-full col-span-9 flex items-center">
        <UilSearch className="text-base text-main absolute ml-4" size={22} />
        <Input
          type="text"
          className="bg-white rounded-[20px] w-[67vw] shadow-box px-12 h-[50px] focus:outline-none placeholder:text-sm"
          placeholder="환자 번호나 이름으로 검색하기"
          onKeyPress={onKeyPress}
          value={keyword}
          onChange={onChangeInput}
        />
      </div>
      <div className="btn-box col-span-1 h-[50px]">
        <Btn
          className="text-white font-semibold bg-main shadow-loginbtn rounded-[20px] w-[8vw] h-full"
          onClick={onSearch}
          content="검색"
        />
      </div>
    </div>
  );
}

export default PatientSearchBar;
