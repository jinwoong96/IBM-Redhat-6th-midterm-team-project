import { Lock, TrendingUp, User } from 'lucide-react';
import React from 'react';
import FormHeader from '../common/form/FormHeader';
import FormTextInput from '../common/form/FormTextInput';
import FormButton from '../common/form/FormButton';
import AuthFooter from '../common/form/AuthFooter';

const LoginForm = () => {
    return (
        <div className="w-full max-w-sm rounded-2xl border border-gray-200 bg-white px-8 py-10 shadow-sm">
            <FormHeader icon={<TrendingUp className="h-8 w-8 text-blue-500"/>} 
                        title={"로그인"}
                        content={"모의 주식 투자에 오신 것을 환영합니다"} />
            <form className='mt-8 space-y-4'>
                <FormTextInput type={"text"} label={"아이디"} icon={<User className="mr-2 h-4 w-4 text-gray-400" />} placeholder={"kosdaqlover"} />
                <FormTextInput type={"password"} label={"비밀번호"} icon={<Lock className="mr-2 h-4 w-4 text-gray-400"/>} placeholder={"••••••••"} />
                <FormButton content={"로그인"} onClick={()=>{alert("로그인 함수 실행")}} />
            </form>
            <AuthFooter type={"login"} />
        </div>
    );
};

export default LoginForm;