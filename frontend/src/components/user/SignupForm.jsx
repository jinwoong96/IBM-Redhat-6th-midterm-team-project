import React from 'react';
import { AtSign, Lock, TrendingUp, User } from 'lucide-react';
import FormHeader from '../common/form/FormHeader';
import FormTextInput from '../common/form/FormTextInput';
import FormButton from '../common/form/FormButton';
import AuthFooter from '../common/form/AuthFooter';

const SignupForm = () => {
    return (
        <div className="w-full max-w-sm rounded-2xl border border-gray-200 bg-white px-8 py-10 shadow-sm">
            <FormHeader icon={<TrendingUp className="h-8 w-8 text-blue-500" />}
                        title={"회원가입"}
                        content={"투자 여정을 시작하세요"} />
            <form className='mt-8 space-y-4'>
                <FormTextInput type={"text"} label={"아이디"} icon={<User className="mr-2 h-4 w-4 text-gray-400" />} placeholder={"kosdaqlover"} />
                <FormTextInput type={"text"} label={"닉네임"} icon={<AtSign className="mr-2 h-4 w-4 text-gray-400"/>} placeholder={"코스닥러버"} />
                <FormTextInput type={"password"} label={"비밀번호"} icon={<Lock className="mr-2 h-4 w-4 text-gray-400"/>} placeholder={"••••••••"} />
                <FormTextInput type={"password"} label={"비밀번호 확인"} icon={<Lock className="mr-2 h-4 w-4 text-gray-400"/>} placeholder={"••••••••"} />
                <FormButton content={"가입하기"} onClick={()=>{alert("회원가입 함수 실행")}} />
            </form>
            <AuthFooter type={"signup"} />
        </div>
    );
};

export default SignupForm;